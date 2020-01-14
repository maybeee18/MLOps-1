import os
from azureml.pipeline.core import PublishedPipeline
from azureml.core import Experiment
from dotenv import load_dotenv
import models.utils.AzureMLUtils as AzureMLUtils

def main():
    load_dotenv()
    ws = AzureMLUtils.get_workspace()
    print("got workspace")
    pipeline_id = os.environ.get("PIPELINE_ID")
    print("PIPELINE_ID !!!!: ",pipeline_id)
    published_pipeline = PublishedPipeline.get(workspace=ws, id=pipeline_id)
    pipeline_run = Experiment(ws, 'batch-run-code').submit(published_pipeline)
    pipeline_run.wait_for_completion(show_output=True)

if __name__ == "__main__":
    main()