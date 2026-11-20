# AI Toll Plaza Vehicle Detection — Progress Report

**Report date:** 20 November 2026  
**Project:** AI-based vehicle detection and classification for toll-plaza monitoring  
**Current stage:** Environment setup completed; initial YOLOv8 training started

---

## 1. Project objective

Develop a prototype that detects and classifies vehicles in toll-plaza imagery and, in later stages, processes CCTV/video footage for vehicle tracking and counting.

Planned workflow:
1. Prepare and validate a vehicle-detection dataset.
2. Train an object-detection model.
3. Evaluate performance on unseen images.
4. Extend the system to video using object tracking.
5. Count each vehicle once when it crosses a virtual line.
6. Later test on relevant Pakistani toll-plaza footage and compare counts with available toll records.

## 2. Dataset preparation

A six-class prototype dataset was prepared from the available Roboflow dataset.

**Source dataset:** `Toll.v2i.yolov8`  
**Prepared dataset:** `G:\AI Roadmap\AI Toll Plaza\Toll_Prototype_6Class`

```text
Toll_Prototype_6Class/
├── data.yaml
├── preparation_report.md
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

**Dataset summary**
- Prepared images: 4,555
- Annotations/boxes: 4,568
- Training split: 3,137 images
- Validation split: 692 images
- Test split: 726 images
- 10 extra-camera images were held out.
- Labels were remapped to six class IDs; image files and bounding-box coordinates were preserved.
- Automated checks reported valid image/label pairs, paths, class IDs, and normalized bounding-box coordinates.

### Six target classes

| Class ID | Vehicle class |
|---:|---|
| 0 | CNG-TEMPU-AUTO |
| 1 | Heavy-Truck |
| 2 | Medium-Truck |
| 3 | Micro-Bus-4Wheeler |
| 4 | Mini-Bus-Coaster |
| 5 | Motor-Cycle |

The dataset YAML defines `nc: 6` and the train, validation, and test image folders.

### Dataset limitations

- The source imagery appears to be from Bangladesh, not Pakistan.
- Some classes in the original 12-class dataset had only one example and were excluded.
- Some vehicle groups have camera/resolution differences.
- Some background vehicles may be unlabelled.
- Mini-Bus-Coaster has fewer training examples than the other retained classes.

These limitations must be considered when interpreting results. This dataset supports an initial prototype experiment, but does not establish performance on Pakistani toll-plaza footage.

## 3. Development environment

The Python virtual environment is located at:

`G:\AI Roadmap\AI Toll Plaza\Toll Test\toll_env`

| Component | Version / details | Status |
|---|---|---|
| Python | 3.12.10 | Verified |
| PyTorch | 2.10.0+cu126 | Installed |
| CUDA availability | `torch.cuda.is_available() == True` | Verified |
| GPU | NVIDIA GeForce GTX 1050, 3 GB VRAM | Detected |
| TorchVision | 0.25.0+cu126 | Installed |
| Ultralytics | 8.4.216 | Installed |
| OpenCV | Installed | Available |

The NVIDIA driver reports CUDA 13.0 compatibility. PyTorch was installed with the CUDA 12.6 wheel, suitable for the GTX 1050's Pascal architecture. A separate CUDA Toolkit installation was not required for this PyTorch setup.

## 4. Initial model test

- Loaded the pretrained `yolov8n.pt` (YOLOv8 Nano) model.
- Ran inference on the sample bus image supplied by Ultralytics.
- Used the NVIDIA GPU (`device=0`) and image size 416.
- The inference test completed.

This verified that the Ultralytics model can be loaded and used for inference in the configured environment.

## 5. Initial training

An initial YOLOv8 Nano training run was launched with this configuration:

| Parameter | Value |
|---|---|
| Model | `yolov8n.pt` |
| Dataset | `Toll_Prototype_6Class/data.yaml` |
| Epochs | 50 |
| Image size | 416 |
| Batch size | 2 |
| Device | NVIDIA GPU (`device=0`) |
| Workers | 0 |

The system monitor showed activity on the NVIDIA GTX 1050 during the training session, with a reported GPU temperature of approximately 60°C at the time of the screenshot.

**Training status:** Training was initiated. Final completion status, epoch results, validation metrics, and saved checkpoint paths still need to be recorded after the run finishes.

## 6. Hardware

- CPU: Intel Core i5, 9th generation
- RAM: 32 GB
- GPU: NVIDIA GeForce GTX 1050, 3 GB VRAM
- Integrated graphics: Intel UHD Graphics

A lightweight YOLOv8 Nano model and conservative initial settings are being used because the GPU has 3 GB VRAM.

## 7. Next steps

1. Allow the initial 50-epoch training run to finish.
2. Record training results and validation metrics: precision, recall, mAP50, and mAP50-95.
3. Review training curves and confusion matrix; inspect false positives and missed detections.
4. Evaluate the best checkpoint on the held-out test split.
5. Save the best model checkpoint and document its results.
6. Test on additional toll-plaza images, preferably from Pakistan, to assess generalization.
7. After image-based evaluation, move to video inference, tracking (e.g. ByteTrack), and virtual-line vehicle counting.

## 8. Current conclusion

The dataset has been converted into a six-class YOLO-format prototype dataset. The Python environment, PyTorch CUDA support, NVIDIA GPU detection, Ultralytics installation, and pretrained YOLOv8 inference test have all been verified. The first custom training run has been started.

No final accuracy or model-performance claim is made at this stage. Those conclusions will be added after training and evaluation are complete.
