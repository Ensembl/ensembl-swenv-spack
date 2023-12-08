# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlClonePp(PerlPackage):
    """Recursively copy Perl datatypes"""

    homepage = "https://metacpan.org/pod/Clone::PP"
    url = "https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-1.08.tar.gz"

    maintainers("EbiArnie")

    version("1.08", sha256="57203094a5d8574b6a00951e8f2399b666f4e74f9511d9c9fb5b453d5d11f578")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
