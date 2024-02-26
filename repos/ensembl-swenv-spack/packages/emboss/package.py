# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Emboss(AutotoolsPackage):
    """EMBOSS is a free Open Source software analysis package specially
    developed for the needs of the molecular biology (e.g. EMBnet) user
    community"""

    homepage = "http://emboss.sourceforge.net/"
    url = "ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz"

    version("6.6.0", sha256="7184a763d39ad96bb598bfd531628a34aa53e474db9e7cac4416c2a40ab10c6e")
    patch("emboss6.6.0.gcc12.patch",
            sha256="5ba10468c1d303789d66e20c85eba3bd3c5d1fed91649af1b5416e8e14fb1a6c")

    depends_on("libxpm")
    depends_on("libgd")
    depends_on("postgresql")

    @run_after("configure")
    def skip_update_checks(self):
        # Delete $(bindir)/embossupdate to skip update checks
        filter_file("$(bindir)/embossupdate", "", "Makefile", string=True)
