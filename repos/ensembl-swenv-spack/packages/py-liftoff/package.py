# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *

class PyLiftoff(PythonPackage):
    """Liftoff is an accurate mapper for gene annotations.
    It can accurately map annotations in GFF or GTF between assemblies of the
    same, or closely-related species. Unlike current coordinate lift-over tools
    which require a pre-generated “chain” file as input, Liftoff is a standalone
    tool that takes two genome assemblies and a reference annotation as input
    and outputs an annotation of the target genome."""

    homepage = "https://github.com/agshumate/Liftoff"
    pypi = "Liftoff/Liftoff-1.6.3.2.tar.gz"

    maintainers = ["EbiArnie"]

    version("1.6.3.2", sha256="7070a861144d0f043533893d39f95589a64d63f0365a99d06d71f1700b7fb758")

    depends_on("py-setuptools", type="build")

    # Tested with 2.17 and 2.24, 2.26
    depends_on("minimap2@2.17:2.26", type=("build", "run"))

    depends_on("py-biopython@1.76:", type=("build", "run"))
    depends_on("py-gffutils@0.10.1:", type=("build", "run"))
    depends_on("py-interlap@0.2.6:", type=("build", "run"))
    depends_on("py-networkx@2.4:", type=("build", "run"))
    depends_on("py-numpy@1.22.0:", type=("build", "run"))
    depends_on("py-parasail@1.2.1:", type=("build", "run"))
    depends_on("py-pyfaidx@0.5.8:", type=("build", "run"))
    depends_on("py-pysam@0.19.1:", type=("build", "run"))
    depends_on("py-ujson@3.2.0:", type=("build", "run"))

