# LinLin Zhang AT Project

This repository contains a collection of tools and frameworks for video processing and analysis, including TimeSformer implementation and RoboVoxel visualization tools.

## Project Structure

```
.
├── beam_frames/           # Directory containing sequential frame images
├── TimeSformer/          # Video transformer implementation
│   ├── configs/          # Configuration files
│   ├── tools/           # Utility scripts
│   ├── timesformer/     # Core TimeSformer implementation
│   └── slurm_scripts/   # SLURM job scripts
└── RoboVoxel/           # Visualization tools
    ├── taichi2d/        # 2D visualization components
    ├── taichi3d/        # 3D visualization components
    └── images/          # Image assets
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- CUDA-compatible GPU (recommended)
- Conda package manager

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Set up the TimeSformer environment:
```bash
cd TimeSformer
conda env create -f environment.yml
conda activate timesformer
```

3. Install TimeSformer package:
```bash
pip install -e .
```

## Dependencies

The main dependencies include:
- PyTorch >= 1.6
- torchvision >= 0.7
- OpenCV >= 4.2
- NumPy > 1.19
- Pandas >= 1.2
- scikit-learn >= 0.22
- JupyterLab
- TensorBoard
- Additional dependencies listed in TimeSformer/environment.yml

## Usage

### TimeSformer

The TimeSformer implementation is located in the `TimeSformer` directory. You can find example usage in `TimeSformer/example.ipynb`.

### RoboVoxel

RoboVoxel provides visualization tools for both 2D and 3D data:
- 2D visualization tools are in `RoboVoxel/taichi2d/`
- 3D visualization tools are in `RoboVoxel/taichi3d/`

### Frame Processing

The `beam_frames` directory contains sequential frame images that can be processed using the provided tools.

## Contributing

Please refer to the following files for contribution guidelines:
- `TimeSformer/CONTRIBUTING.md`
- `TimeSformer/CODE_OF_CONDUCT.md`

## License

This project is licensed under the terms specified in `TimeSformer/LICENSE`.

## Support

For issues and questions, please open an issue in the repository's issue tracker. 