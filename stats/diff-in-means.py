# to run in venv on windows, `source Scripts/activate` from `stats` dir

import sys
import pandas
from scipy import stats

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
# TODO: all 8 tests u skipped the first time lol, with DRY code
def runAllMeanDiffTests(df):
    if len(sys.argv) > 1 and sys.argv[1].lower() == "dump_df=true":
        print("dumping df:")
        print(df)

    print("mbps down overall")
    mbps_down_orbi_legacy = df[df.mesh_config == "orbi_legacy"].mbps_down
    mbps_down_orbi_rbs50v2 = df[df.mesh_config == "orbi_rbs50v2"].mbps_down
    ttest, pval = stats.ttest_ind(mbps_down_orbi_legacy,mbps_down_orbi_rbs50v2)
    mean_diff = mbps_down_orbi_legacy.mean() - mbps_down_orbi_rbs50v2.mean()
    print("pval, diff in means, mbps down, overall: " + str(pval))
    print("mean diff, orbi_legacy-orbi_rbs50v2, mbps down, overall: " + str(mean_diff))

    # result note: new config uploads mbps ~110mbps faster, stat significant at alpha < 0.05
    print("mbps up overall")
    mbps_up_orbi_legacy = df[df.mesh_config == "orbi_legacy"].mbps_up
    mbps_up_orbi_rbs50v2 = df[df.mesh_config == "orbi_rbs50v2"].mbps_up
    ttest, pval = stats.ttest_ind(mbps_up_orbi_legacy,mbps_up_orbi_rbs50v2)
    mean_diff = mbps_up_orbi_legacy.mean() - mbps_up_orbi_rbs50v2.mean()
    print("pval, diff in means, mbps up, overall: " + str(pval))
    print("mean diff, orbi_legacy-orbi_rbs50v2, mbps up, overall: " + str(mean_diff))

    print("mean diff latency overall")

    print("mean diff down mb three-cxn")
    print("mean diff up mb three-cxn")
    print("mean diff latency three-cxn")

    print("mean diff down mb three-cxn-without-outlier")
    print("mean diff up mb three-cxn-without-outlier")
    print("mean diff latency three-cxn-without-outlier")

    return "foobar"

main()
