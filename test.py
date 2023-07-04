import os
os.environ["PROMPTFLOW_CONNECTIONS"] = "connections.json"

import promptflow as pf
from promptflow import load_flow
from promptflow.core.connection_manager import ConnectionManager

# Local run
flow = load_flow(source=r"./web_classification")
data_path = "./webClassification3.jsonl"
connections = {"azure_open_ai_connection": ConnectionManager().get("azure_open_ai_connection")}
baseline = flow.run_bulk(input=data_path, connections=connections, output="./basic_eval_bulk")
pf.show_details(baseline)


# Remote submit
import promptflow.azure as pf
from promptflow.azure import load_flow
# configure azureml workspace ml_client
from azure.ai.ml import MLClient
from azure.identity import InteractiveBrowserCredential

client = MLClient(
    credential=InteractiveBrowserCredential(),
    subscription_id="96aede12-2f73-41cb-b983-6d11a904839b",
    resource_group_name="sdk",
    workspace_name="migration-test",
)
pf.configure(client=client)

flow = load_flow(source=r"./web_classification")
data_path = "./webClassification3.jsonl"
connections = {"azure_open_ai_connection": ConnectionManager().get("azure_open_ai_connection")}
baseline = flow.submit_bulk_run(data=data_path, connections=connections, output="./basic_eval_bulk", runtime="ci_runtime2")
pf.show_details(baseline)