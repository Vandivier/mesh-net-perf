# to run in venv on windows, `source Scripts/activate` from `stats` dir

import sys
import pandas
import statsmodels

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix

def main():
    print("in venv: " + str(in_virtualenv()))
    df = pandas.read_csv("./input-data.csv")
    diffInMeansTestResult = runAllMeanDiffTests(df)
    print("diffInMeansTestResult: " + str(diffInMeansTestResult))

# TODO: have this print a csv or json file for web app consumption (file-based handoff)
def runAllMeanDiffTests(df):
    print("dumping df summary:")
    print(str(df))

    print("mean diff down mb overall")
    print("mean diff up mb overall")
    print("mean diff latency overall")

    print("mean diff down mb three-cxn")
    print("mean diff up mb three-cxn")
    print("mean diff latency three-cxn")

    print("mean diff down mb three-cxn-without-outlier")
    print("mean diff up mb three-cxn-without-outlier")
    print("mean diff latency three-cxn-without-outlier")

    return "foobar"

main()
