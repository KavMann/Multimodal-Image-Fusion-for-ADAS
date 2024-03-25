import subprocess

# Command to execute
command = 'yolo task=detect mode=predict model="../Multimodal-Image-Fusion/runs/train-ir/weights/best.pt" source="../Multimodal-Image-Fusion/videos/IR/set-9.mp4" conf=0.3 save=True'

# Execute the command
subprocess.run(command, shell=True)
