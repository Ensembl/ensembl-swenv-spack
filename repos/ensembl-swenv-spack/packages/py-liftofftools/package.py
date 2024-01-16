# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *

class PyLiftofftools(PythonPackage):
    """LiftoffTools is a toolkit to compare genes lifted between genome assemblies."""

    homepage = "https://github.com/agshumate/LiftoffTools"
    pypi = "LiftoffTools/LiftoffTools-0.4.4.tar.gz"

    maintainers("EbiArnie")

    version("0.4.4", sha256="eba2fe460e9f824546145b6193a0d3e855aa1f11fb7062f2abac11b7cff1eda8")

    depends_on("python@3.6:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("mmseqs2@14:", type=("build", "run"))
    depends_on("py-biopython@1.76:", type=("build", "run"))
    depends_on("py-gffutils@0.10.1:", type=("build", "run"))
    depends_on("py-liftoff@1.6.3.2:", type=("build", "run"))
    depends_on("py-matplotlib@3.5.2:", type=("build", "run"))
    depends_on("py-nltk@3.6.7:", type=("build", "run"))
    depends_on("py-numpy@1.21.1:", type=("build", "run"))
    depends_on("py-parasail@1.2.4:", type=("build", "run"))
    depends_on("py-pyfaidx@0.5.8:", type=("build", "run"))
