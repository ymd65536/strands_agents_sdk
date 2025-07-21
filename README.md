# Strands Agents

## Setup

```bash
aws configure sso --profile default
```

リージョンは`ap-northeast-1`、出力形式は`json`にします。

```bash
export AWS_DEFAULT_REGION=us-west-2
```

```bash
aws sts get-caller-identity
```

## Run

デフォルトではus-west-2のClaude 4 Sonnetが使われます。
bedrockのモデルを使う場合はstrands.modelsというパッケージからBedrockModelクラスをインポートします。
