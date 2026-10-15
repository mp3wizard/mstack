#!/usr/bin/env python3
"""System Usability Scale (Brooke 1996) scorer.

Each respondent answers 10 items on a 1-5 scale. Odd items score (answer - 1),
even items score (5 - answer). The sum times 2.5 gives 0-100. A SUS score is not
a percentage. About 68 is the average, near the 50th percentile, so compare the
interval to that benchmark, not to 100.

Usage:
  sus.py "5,1,5,1,5,1,5,1,5,1" "4,2,4,2,4,2,4,2,4,2" ...
  sus.py --self-test
"""
import statistics
import sys

BENCHMARK = 68.0
# Two-sided 95% t critical values by degrees of freedom. Above 30, use z.
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306,
       9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
       16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074,
       23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048, 29: 2.045, 30: 2.042}


def score(answers):
    if len(answers) != 10 or any(a not in (1, 2, 3, 4, 5) for a in answers):
        raise ValueError(f"need 10 answers in 1..5, got {answers}")
    total = sum((a - 1) if i % 2 == 0 else (5 - a) for i, a in enumerate(answers))
    return total * 2.5


def interval(scores):
    """Mean and two-sided 95% t interval, clamped to 0..100."""
    n = len(scores)
    mean = statistics.mean(scores)
    if n < 2:
        return mean, None
    t = T95.get(n - 1, 1.96)
    half = t * statistics.stdev(scores) / n ** 0.5
    return mean, (max(0.0, mean - half), min(100.0, mean + half))


def verdict(ci):
    lo, hi = ci
    if lo > BENCHMARK:
        return f"above the {BENCHMARK:.0f} benchmark"
    if hi < BENCHMARK:
        return f"below the {BENCHMARK:.0f} benchmark"
    return f"not distinguishable from the {BENCHMARK:.0f} benchmark"


def self_test():
    assert score([5, 1] * 5) == 100.0, "best answers score 100"
    assert score([1, 5] * 5) == 0.0, "worst answers score 0"
    assert score([3] * 10) == 50.0, "all neutral scores 50"
    try:
        score([3] * 9)
        raise AssertionError("9 answers accepted")
    except ValueError:
        pass
    mean, ci = interval([70.0, 80.0, 90.0])
    assert mean == 80.0, "mean of 70, 80, 90"
    assert abs(ci[0] - 55.16) < 0.01 and abs(ci[1] - 100.0) < 0.01, f"t interval with df=2, got {ci}"
    assert interval([60.0])[1] is None, "one respondent has no interval"
    assert verdict((70.0, 90.0)).startswith("above"), "interval above 68"
    assert verdict((60.0, 75.0)).startswith("not distinguishable"), "interval spans 68"
    print("sus.py self-test: ok")


def main(argv):
    if argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    scores = [score([int(x) for x in row.split(",")]) for row in argv[1:]]
    for i, s in enumerate(scores, 1):
        print(f"respondent {i}: {s:.1f}")
    mean, ci = interval(scores)
    if ci is None:
        print(f"n=1 score={mean:.1f}. One respondent gives no interval. Do not report it as a SUS result.")
        return 0
    print(f"n={len(scores)} mean={mean:.1f} 95% CI {ci[0]:.1f} to {ci[1]:.1f}, {verdict(ci)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
