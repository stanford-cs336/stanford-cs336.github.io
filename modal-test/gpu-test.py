# import modal
#
# image = modal.Image.debian_slim().uv_sync()
# modal.Image
# app = modal.App(image=image)
#
#
# @app.function(gpu="A100")
# def run():
#     import torch
#
#     assert torch.cuda.is_available()
#
#     a = torch.tensor([[1, 2, 3], [4, 5, 6]]).to("cuda")
#     print(a.device)
#     print(a * 2)

# +

import torch

torch.cuda.is_available()

# +

a = torch.tensor([[1, 2, 3], [4, 5, 6]]).to("cuda")
a * 2
