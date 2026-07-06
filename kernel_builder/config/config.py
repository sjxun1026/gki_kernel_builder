from pathlib import Path
from typing import Final, Literal

from kernel_builder.constants import ROOT

# ---- Build Info
KERNEL_NAME: Final[str] = "ESK"
DEFCONFIG: Final[str] = "gki_defconfig"
BUILD_USER: Final[str] = "gki-builder"
BUILD_HOST: Final[str] = "esk"
IMAGE_COMP: Final[Literal["raw", "lz4", "gz"]] = "gz"

# ---- Kernel
KERNEL_REPO: Final[str] = "android.googlesource.com:kernel/common"
KERNEL_BRANCH: Final[str] = "android14-6.1"

# ---- AnyKernel3
ANYKERNEL_REPO = "github.com:bachnxuan/AnyKernel3"
ANYKERNEL_BRANCH = "android14-6.1"

# ---- Release
RELEASE_REPO: Final[str] = "android.googlesource.com:kernel/common"
RELEASE_BRANCH: Final[str] = "android14-6.1"

# ---- Clang
CLANG_VARIANT: Final[Literal["SLIM", "AOSP", "RV", "YUKI", "LILIUM", "NEUTRON"]] = (
    "AOSP"
)

# Optional: Set custom clang link (override CLANG_VARIANT)
CLANG_URL: str | None = None

# ---- Boot Image Config
BOOT_SIGNING_KEY: Final[Path] = ROOT / "key" / "key.pem"
GKI_URL: Final[str] = (
    "https://dl.google.com/android/gki/gki-certified-boot-android14-6.1-2024-03_r1.zip"
)

# ---- Logging
LOGFILE: Final[str | Path | None] = None

if __name__ == "__main__":
    raise SystemExit("This file is meant to be imported, not executed.")
