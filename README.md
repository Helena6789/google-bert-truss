# Deploying LLM Into Production

This repo contains the code needed to run [pre-trained BERT](https://huggingface.co/google-bert/bert-base-uncased) from Hugging Face sing Truss and containerize it using Docker.

### Install

```bash
pip install -r requirements.txt
```

### Deploy

To deploy the model on the cluster, create a Kubernetes deployment and service using the provided YAML files `truss-bert-deployment.yaml`.