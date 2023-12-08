# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *

class PyGffpandas(PythonPackage):
    """GFF annotations in panda dataframes"""

    homepage = "https://github.com/foerstner-lab/gffpandas"
    pypi = "gffpandas/gffpandas-1.2.0.tar.gz"

    maintainers("EbiArnie")

    version("1.2.0", sha256="1a1e1c5c5120bf46ec57517222ebb42ffaab3f768c972fec54c4ac1b07b7f0c6")

    depends_on("py-setuptools", type="build")
    depends_on("py-pandas", type=("build", "run"))
