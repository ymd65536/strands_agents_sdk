# us-east-1の基盤モデルを取得するサンプルコード
import boto3

bedrock_client = boto3.client("bedrock",region_name="us-west-2")
bedrock_found_list = bedrock_client.list_foundation_models()
model_summaries = bedrock_found_list['modelSummaries']

for model_summary in model_summaries:
    print(model_summary['modelArn'])

