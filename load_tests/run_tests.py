import uuid
import requests
from multiprocessing import Pool
from load_tests.inputs import TECH_EO_INPUT, TECH_EO_EXCESS_INPUT, CYBER_EXCESS_INPUT, CYBER_INPUT

count = 0


def create_calculate_request(port: str, api: str, input_data: dict, risk_model: str):
    try:
        correlation_id: str = str(uuid.uuid4())
        target = "http://localhost:{}/api/risk/quick_quote/{}".format(port, api)
        res = requests.post(url=target, json=input_data,
                            headers={"X-Risk-Model-Version": risk_model, "X-Correlation-ID": correlation_id,
                                     'Accept': "application/json", "Content-Type": "application/json"},
                            verify=False)
        return res
    except Exception as e:
        print("request failed - api: {}: {}".format(api, e))


def run_tests_calc_tech(port: str):
    global count
    product: str = "Tech E&O Risk Model v1.11.0"
    res = create_calculate_request(port, "calculate", TECH_EO_INPUT, product)
    if res.status_code == 200:
        print("Test number {} - success - {} - {}".format(count, "calculate", product))
    else:
        print("Test number {} - failed - {} - {}".format(count, "calculate", product))
    count += 1


def run_tests_bs_hz_tech(port: str):
    global count
    product: str = "Tech E&O Risk Model v1.11.0"
    res = create_calculate_request(port, "business_class_hazard_group", TECH_EO_INPUT, product)
    if res.status_code == 200:
        print("Test number {} - success - {} - {}".format(count, "business_class_hazard_group", product))
    else:
        print("Test number {} - failed - {} - {}".format(count, "business_class_hazard_group", product))
    count += 1


def run_tests_calc_tech_excess(port: str):
    global count
    product: str = "Excess Tech E&O Risk Model v1.11.0"
    res = create_calculate_request(port, "calculate", TECH_EO_EXCESS_INPUT, product)
    if res.status_code == 200:
        print("Test number {} - success - {} - {}".format(count, "calculate", product))
    else:
        print("Test number {} - failed - {} - {}".format(count, "calculate", product))
    count += 1


def run_tests_bs_hz_tech_excess(port: str):
    global count
    product: str = "Excess Tech E&O Risk Model v1.11.0"
    res = create_calculate_request(port, "business_class_hazard_group", TECH_EO_EXCESS_INPUT, product)
    if res.status_code == 200:
        print("Test number {} - success - {} - {}".format(count, "business_class_hazard_group", product))
    else:
        print("Test number {} - failed - {} - {}".format(count, "business_class_hazard_group", product))
    count += 1


def run_tests_calc_cyber_excess(port: str):
    global count
    product: str = "Excess Cyber Risk Model v1.11.0"
    res = create_calculate_request(port, "calculate", CYBER_EXCESS_INPUT, product)
    if res.status_code == 200:
        print("Test number {} - success - {} - {}".format(count, "calculate", product))
    else:
        print("Test number {} - failed - {} - {}".format(count, "calculate", product))
    count += 1


def run_tests_calc_cyber(port: str):
    global count
    product: str = "Cyber Risk Model v1.11.0"
    res = create_calculate_request(port, "calculate", CYBER_INPUT, product)
    if res.status_code == 200:
        print("Test number {} - success - {} - {}".format(count, "calculate", product))
    else:
        print("Test number {} - failed - {} - {}".format(count, "calculate", product))
    count += 1


if __name__ == '__main__':

    # Define the dataset
    dataset = ["5006" for i in range(0, 50)]

    # Run this with a pool of 10 agents having a chunksize of 3 until finished
    agents = 10
    chunksize = 5
    with Pool(processes=agents) as pool:
        pool.map(run_tests_calc_tech_excess, dataset, chunksize)
    with Pool(processes=agents) as pool:
        pool.map(run_tests_bs_hz_tech_excess, dataset, chunksize)
    with Pool(processes=agents) as pool:
        pool.map(run_tests_calc_tech, dataset, chunksize)
    with Pool(processes=agents) as pool:
        pool.map(run_tests_bs_hz_tech, dataset, chunksize)
    with Pool(processes=agents) as pool:
        pool.map(run_tests_calc_cyber_excess, dataset, chunksize)
    with Pool(processes=agents) as pool:
        pool.map(run_tests_calc_cyber, dataset, chunksize)
