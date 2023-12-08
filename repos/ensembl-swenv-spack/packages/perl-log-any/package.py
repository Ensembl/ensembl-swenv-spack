# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLogAny(PerlPackage):
    """Bringing loggers and listeners together"""

    homepage = "https://metacpan.org/pod/Log::Any"
    url = "https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-1.717.tar.gz"

    maintainers("EbiArnie")

    version("1.717", sha256="56649da0f3900230c9e3d29252cb0a74806fb2ddebd22805acd7368959a65bca")


    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
