<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/litserveLogo.png" alt="LitGPT" height="90px"/>

&nbsp;

# LitServe

**High-throughput serving engine for AI models**

<pre>
✅ Batching       ✅ Streaming          ✅ Auto-GPU, multi-GPU 
✅ Multi-modal    ✅ PyTorch/JAX/TF     ✅ Full control        
✅ Auth           ✅ Built on Fast API                         
</pre>



---


<p align="center">

<a target="_blank" href="https://lightning.ai/lightning-ai/studios/litserve-hello-world">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/>
</a>

</p>

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/litserve)
![cpu-tests](https://github.com/Lightning-AI/litserve/actions/workflows/ci-testing.yml/badge.svg) [![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/litserve/blob/main/LICENSE) [![Discord](https://img.shields.io/discord/1077906959069626439?style=plastic)](https://discord.gg/VptPCZkGNa)


<p align="center">
  <a href="https://lightning.ai/">Lightning AI</a> •
  <a href="#get-started">Get started</a> •
  <a href="#examples">Examples</a> •
  <a href="#features">Features</a>
</p>

</div>

&nbsp;

# Deploy AI models Lightning fast ⚡
LitServe is a high-throughput serving engine for deploying AI models at scale. LitServe generates an API endpoint for a model, handles batching, streaming, autoscaling across CPU/GPUs and more.

Why we wrote LitServe:

1. Work with any model: LLMs, vision, time-series, etc...
3. We wanted a zero abstraction, minimal, hackable code-base without bloat.
5. Built for enterprise scale (not demos, etc...).
6. Easy enough for researchers, scalable and hackable for engineers.
2. Work on any hardware (GPU/TPU) automatically.
5. Let you focus on model performance, not the serving boilerplate.

Think of LitServe as PyTorch Lightning for model serving (if you're familiar with Lightning) but supports every framework like PyTorch, JAX, Tensorflow and more.

<div align="center">
    <img src="https://github.com/Lightning-AI/litserve/assets/3640001/4a4a5028-1e64-46f3-b0db-ef5b3f636655" height="160px">
</div>

&nbsp;

# Examples
Explore various examples that show different models deployed with LitServe:

| Example  | description | Run |
|---|---|---|
| [Hello world](#implement-a-server)  | Hello world model | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/litserve-hello-world"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Llama 3 (8B)](https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-8b-api)  | **(LLM)** Deploy Llama 3 | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-8b-api"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [ANY Hugging face model](https://lightning.ai/lightning-ai/studios/deploy-any-hugging-face-model-instantly)  | **(Text)** Deploy any Hugging Face model | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-any-hugging-face-model-instantly"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a> |
| [Hugging face BERT model](https://lightning.ai/lightning-ai/studios/deploy-a-hugging-face-bert-model)  | **(Text)** Deploy model for tasks like text generation and more | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-hugging-face-bert-model"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a>
| [Open AI CLIP](https://lightning.ai/lightning-ai/studios/deploy-open-ai-clip-with-litserve)  | **(Multimodal)** Deploy Open AI CLIP for tasks like image understanding | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-open-ai-clip-with-litserve"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a>
| [Open AI Whisper](https://lightning.ai/lightning-ai/studios/deploy-open-ai-s-whisper-model)  | **(Audio)** Deploy Open AI Whisper for tasks like speech to text | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-open-ai-s-whisper-model"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a>
| [Stable diffusion 2](https://lightning.ai/lightning-ai/studios/deploy-a-private-api-for-stable-diffusion-2)  | **(Vision)** Deploy Stable diffusion 2 for tasks like image generation | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-private-api-for-stable-diffusion-2"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a>
| [Text-speech (XTTS V2)](https://lightning.ai/lightning-ai/studios/deploy-a-voice-clone-api-coqui-xtts-v2-model)  | **(Speech)** Deploy a text to speech voice cloning API. | <a target="_blank" href="https://lightning.ai/lightning-ai/studios/deploy-a-voice-clone-api-coqui-xtts-v2-model"><img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/></a>

&nbsp;

# Install LitServe
Install LitServe via pip:

```bash
pip install litserve
```

<details>
  <summary>Advanced install options</summary>
&nbsp;

Install the main branch:

```bash
pip install git+https://github.com/Lightning-AI/litserve.git@main
```
&nbsp;

Install from source:

```bash
git clone https://github.com/Lightning-AI/litserve
cd litserve
pip install -e '.[all]'
```

</details>

&nbsp;

# Get started
LitServe has a minimal API that allows enterprise-scale, with full control.

1. Implement the LitAPI class which describes the inference process for the model(s).
2. Enable the specific optimizations (such as batching or streaming) in the LitServer.

## Implement a server
Here's a hello world example:

<a target="_blank" href="https://lightning.ai/lightning-ai/studios/litserve-hello-world">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/>
</a>

```python
# server.py
import litserve as ls

# STEP 1: DEFINE YOUR MODEL API
class SimpleLitAPI(ls.LitAPI):
    def setup(self, device):
        # Setup the model so it can be called in `predict`.
        self.model = lambda x: x**2

    def decode_request(self, request):
        # Convert the request payload to your model input.
        return request["input"]

    def predict(self, x):
        # Run the model on the input and return the output.
        return self.model(x)

    def encode_response(self, output):
        # Convert the model output to a response payload.
        return {"output": output}


# STEP 2: START THE SERVER
if __name__ == "__main__":
    api = SimpleLitAPI()
    server = ls.LitServer(api, accelerator="auto")
    server.run(port=8000)
```

Now run the server via the command-line

```bash
python server.py
```

## Use the server
LitServe automatically generates a client when it starts. Use this client to test the server:

```bash
python client.py
```

Or ping the server yourself directly
```python
import requests
response = requests.post("http://127.0.0.1:8000/predict", json={"input": 4.0})
```

The server expects the client to send a `POST` to the `/predict` URL with a JSON payload.
The way the payload is structured is up to the implementation of the `LitAPI` subclass.

&nbsp;

# Features
LitServe supports multiple advanced state-of-the-art features.

| Feature  | description  |
|---|---|
| Accelerators  | CPU, GPU, Multi-GPU, mps  |
| Auto-GPU  | Detects and auto-runs on all GPUs on a machine  |
| Model types  | LLMs, Vision, Time series, any model type...  |
| ML frameworks  | PyTorch, Jax, Tensorflow, numpy, etc...  |
| Batching | ✅ |
| API authentication | ✅ |
| Multiple models in a single API | ✅ |
| Full request/response control | ✅ |
| Automatic schema validation | ✅ |
| Handle timeouts | ✅ |
| Handle disconnects | ✅ |
| Streaming | ✅ |

> [!NOTE]
> Our goal is not to jump on every hype train, but instead support features that scale
under the most demanding enterprise deployments.

## Feature details

Explore each feature in detail:

<details>
    <summary>Use accelerators automatically (GPUs, CPU, mps)</summary>
&nbsp;

LitServe automatically detects GPUs on a machine and uses them when available:

```python
import litserve as ls
from litserve.examples import SimpleLitAPI

# Automatically selects the available accelerator
api = SimpleLitAPI() # defined by you with ls.LitAPI

# when running on GPUs these are equivalent. It's best to let Lightning decide by not specifying it!
server = ls.LitServer(api)
server = ls.LitServer(api, accelerator="cuda")
server = ls.LitServer(api, accelerator="auto")
```

`LitServer` accepts an `accelerator` argument which defaults to `"auto"`. It can also be explicitly set to `"cpu"`, `"cuda"`, or
`"mps"` if you wish to manually control the device placement.

The following example shows how to set the accelerator manually:

```python
import litserve as ls
from litserve.examples import SimpleLitAPI

# Run on CUDA-supported GPUs
server = ls.LitServer(SimpleLitAPI(), accelerator="cuda")

# Run on Apple's Metal-powered GPUs
server = ls.LitServer(SimpleLitAPI(), accelerator="mps")
```

</details>

<details>
  <summary>Serve on multi-GPUs</summary>

&nbsp;

`LitServer` has the ability to coordinate serving from multiple GPUs.

`LitServer` accepts a `devices` argument which defaults to `"auto"`. On multi-GPU machines, LitServe
will run a copy of the model on each device detected on the machine.

The `devices` argument can also be explicitly set to the desired number of devices to use on the machine.

```python
import litserve as ls
from litserve.examples import SimpleLitAPI

# Automatically selects the available accelerators
api = SimpleLitAPI() # defined by you with ls.LitAPI

# when running on a 4-GPUs machine these are equivalent.
# It's best to let Lightning decide by not specifying accelerator and devices!
server = ls.LitServer(api)
server = ls.LitServer(api, accelerator="cuda", devices=4)
server = ls.LitServer(api, accelerator="auto", devices="auto")
```

For example, running the API server on a 4-GPU machine, with a PyTorch model served on each GPU:

```python
import torch, torch.nn as nn
import litserve as ls

class Linear(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
        self.linear.weight.data.fill_(2.0)
        self.linear.bias.data.fill_(1.0)

    def forward(self, x):
        return self.linear(x)

class SimpleTorchAPI(ls.LitAPI):
    def setup(self, device):
        # move the model to the correct device
        # keep track of the device for moving data accordingly
        self.model = Linear().to(device)
        self.device = device

    def decode_request(self, request):
        # get the input and create a 1D tensor on the correct device
        content = request["input"]
        return torch.tensor([content], device=self.device)

    def predict(self, x):
        # the model expects a batch dimension, so create it
        return self.model(x[None, :])

    def encode_response(self, output):
        # float will take the output value directly onto CPU memory
        return {"output": float(output)}


if __name__ == "__main__":
    # accelerator="auto" (or "cuda"), devices="auto" (or 4) will lead to 4 workers serving
    # the model from "cuda:0", "cuda:1", "cuda:2", "cuda:3" respectively
    server = ls.LitServer(SimpleTorchAPI(), accelerator="auto", devices="auto")
    server.run(port=8000)
```

The `devices` argument can also be an array specifying what device id to
run the model on:

```python
import litserve as ls
from litserve.examples import SimpleTorchAPI

server = ls.LitServer(SimpleTorchAPI(), accelerator="cuda", devices=[0, 3])
```

Last, you can run multiple copies of the same model from the same device,
if the model is small. The following will load two copies of the model on
each of the 4 GPUs:

```python
import litserve as ls
from litserve.examples import SimpleTorchAPI

server = ls.LitServer(SimpleTorchAPI(), accelerator="cuda", devices=4, workers_per_device=2)
```

</details>

<details>
  <summary>Timeouts and disconnections</summary>

&nbsp;

The server will remove a queued request if the client requesting it disconnects.

You can configure a timeout (in seconds) after which clients will receive a `504` HTTP
response (Gateway Timeout) indicating that their request has timed out.

For example, this is how you can configure the server with a timeout of 30 seconds per response.

```python
import litserve as ls
from litserve.examples import SimpleLitAPI

server = ls.LitServer(SimpleLitAPI(), timeout=30)
```

This is useful to avoid requests queuing up beyond the ability of the server to respond.


To disable the timeout for long-running tasks, set `timeout=False` or `timeout=-1`:

```python
import litserve as ls
from litserve.examples import SimpleLitAPI

server = ls.LitServer(SimpleLitAPI(), timeout=False)
```

</details>

<details>
  <summary>Use API key authentication</summary>

&nbsp;

In order to secure the API behind an API key, just define the env var when
starting the server

```bash
LIT_SERVER_API_KEY=supersecretkey python main.py
```

Clients are expected to auth with the same API key set in the `X-API-Key` HTTP header.

</details>

<details>
  <summary>Dynamic batching</summary>
&nbsp;

LitServe can combine individual requests into a batch to improve throughput.
To enable batching, you need to set the `max_batch_size` argument to match the batch size that your model can handle
and implement `LitAPI.predict` to process batched inputs.


```python
import numpy as np
import litserve as ls

class SimpleBatchedAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x: x ** 2

    def decode_request(self, request):
        return np.asarray(request["input"])

    def predict(self, x):
        result = self.model(x)
        return result

    def encode_response(self, output):
        return {"output": output}

if __name__ == "__main__":
    api = SimpleBatchedAPI()
    server = ls.LitServer(api, max_batch_size=4, batch_timeout=0.05)
    server.run(port=8000)
```

You can control the wait time to aggregate requests into a batch with the `batch_timeout` argument.
In the above example, the server will wait for 0.05 seconds to combine 4 requests together.

&nbsp;

LitServe automatically stacks NumPy arrays and PyTorch tensors along the batch dimension before calling the
`LitAPI.predict` method, and splits the output across requests afterward. You can customize this behavior by overriding the
`LitAPI.batch` and `LitAPI.unbatch` methods to handle different data types.

```python
import litserve as ls
from litserve.examples import SimpleBatchedAPI
import numpy as np

class CustomBatchedAPI(SimpleBatchedAPI):
    def batch(self, inputs):
        return np.stack(inputs)

    def unbatch(self, output):
        return list(output)

if __name__ == "__main__":
    api = CustomBatchedAPI()
    server = ls.LitServer(api, max_batch_size=4, batch_timeout=0.05)
    server.run(port=8000)
```


</details>


<details>
  <summary>Stream long responses</summary>

&nbsp;

LitServe can stream outputs from the model in real-time, such as returning text one word at a time from a language model.

To enable streaming, you need to set `LitServer(..., stream=True)` and  implement `LitAPI.predict` and `LitAPI.encode_response`
as a generator (a Python function that yields output).

For example, streaming long responses generated over time:

```python
import json
import litserve as ls

class SimpleStreamAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model = lambda x, y: x * y

    def decode_request(self, request):
        return request["input"]

    def predict(self, x):
        for i in range(10):
            yield self.model(x, i)

    def encode_response(self, output):
        for out in output:
            yield json.dumps({"output": out})


if __name__ == "__main__":
    api = SimpleStreamAPI()
    server = ls.LitServer(api, stream=True)
    server.run(port=8000)
```

&nbsp;

</details>

<details>
  <summary>Automatic schema validation</summary>

&nbsp;

Define the request and response as [Pydantic models](https://docs.pydantic.dev/latest/),
to automatically validate the request.

```python
from pydantic import BaseModel
import litserve as ls


class PredictRequest(BaseModel):
    input: float


class PredictResponse(BaseModel):
    output: float


class SimpleLitAPI(ls.LitAPI):
    def setup(self, device):
        self.model = lambda x: x**2

    def decode_request(self, request: PredictRequest) -> float:
        return request.input

    def predict(self, x):
        return self.model(x)

    def encode_response(self, output: float) -> PredictResponse:
        return PredictResponse(output=output)


if __name__ == "__main__":
    api = SimpleLitAPI()
    server = ls.LitServer(api, accelerator="auto")
    server.run(port=8000)
```

</details>


# Contribute
LitServe is a community project accepting contributions. Let's make the world's most advanced AI inference engine.


<details>
  <summary>Run tests</summary>

Use `pytest` to run tests locally.

First, install test dependencies:

```shell
pip install -r _requirements/test.txt
```

Run the tests
```shell
pytest tests
```

</details>

# License

litserve is released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
See LICENSE file for details.
