import torch
from safetensors.torch import load_file

# Main function
def main():
    print("Hello from main!")
    state_dict = load_file("D:/Pinokio/pinokio/api/fluxgym.git/models/unet/flux1-dev.sft")
    
    # Print number of parameters and list of parameter names
    print(f"Loaded {len(state_dict)} parameters.")
    print("Sample keys:", list(state_dict.keys())[:10])  # print only first 10 keys

# Run the script
if __name__ == "__main__":
    main()