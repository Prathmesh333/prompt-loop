"""Evaluate the dedupe exercise against task-level acceptance conditions.

This checks a candidate artifact. It does not automate or independently evaluate
the agent's choice of prompts, counters, or stop conditions.
"""

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path


def evaluate(candidate_path):
    spec = importlib.util.spec_from_file_location("candidate", candidate_path)
    candidate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(candidate)
    shared = {"key": [1]}
    equal_duplicate = {"key": [1]}
    cases = [
        ("empty", [], []),
        ("order", [3, 1, 3, 2, 1], [3, 1, 2]),
        ("strings", ["z", "a", "z"], ["z", "a"]),
        ("lists", [[2], [1], [2]], [[2], [1]]),
        ("dicts", [{"a": 1}, {"b": 2}, {"a": 1}], [{"a": 1}, {"b": 2}]),
        ("mixed", [1, "x", [1], {"k": 2}, 1, [1]], [1, "x", [1], {"k": 2}]),
        ("first_identity", [shared, equal_duplicate], [shared]),
        ("input_unchanged", [[1], [1], [2]], [[1], [2]]),
    ]
    results = []
    for name, values, expected in cases:
        before = copy.deepcopy(values)
        try:
            output = candidate.dedupe(values)
            passed = isinstance(output, list) and output == expected and values == before
            if name == "first_identity":
                passed = passed and output[0] is shared
            results.append({"check": name, "pass": passed, "output": output})
        except Exception as exc:
            results.append({"check": name, "pass": False, "error": f"{type(exc).__name__}: {exc}"})
    return {
        "candidate": str(candidate_path.resolve()),
        "sha256": hashlib.sha256(candidate_path.read_bytes()).hexdigest(),
        "passed": sum(row["pass"] for row in results),
        "total": len(results),
        "checks": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    result = evaluate(args.candidate)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['passed']}/{result['total']} checks passed; report: {args.report.resolve()}")
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
