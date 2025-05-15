import os
from dotenv import load_dotenv
import replicate
load_dotenv()

def make_input_dict(garm_img:str, human_img, desc:str)->dict:
    input = {
        "garm_img": garm_img,
        "human_img": human_img,
        "garment_des": desc
        }
    return input


def get_model_output(input:dict):
    output = replicate.run(
    "cuuupid/idm-vton:0513734a452173b8173e907e3a59d19a36266e55b48528559432bd21c7d7e985",
    input=input
    )

    with open("output.jpg", wb) as file:
        file.write(output.read())