# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlioGzip(PerlPackage):
    """Perl extension to provide a PerlIO layer to gzip/gunzip"""

    homepage = "https://metacpan.org/pod/PerlIO::gzip"
    url = "https://cpan.metacpan.org/authors/id/N/NW/NWCLARK/PerlIO-gzip-0.20.tar.gz"

    maintainers("EbiArnie")

    version("0.20", sha256="4848679a3f201e3f3b0c5f6f9526e602af52923ffa471a2a3657db786bd3bdc5")


    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
