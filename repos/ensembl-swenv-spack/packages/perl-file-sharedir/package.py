# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFileSharedir(PerlPackage):
    """Locate per-dist and per-module shared files"""

    homepage = "https://metacpan.org/pod/File::ShareDir"
    url = "https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-ShareDir-1.118.tar.gz"

    maintainers("EbiArnie")

    version("1.118", sha256="3bb2a20ba35df958dc0a4f2306fc05d903d8b8c4de3c8beefce17739d281c958")

    depends_on("perl-class-inspector@1.12:", type=("run"))
    depends_on("perl-file-sharedir-install@0.13:", type=("build", "link"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
