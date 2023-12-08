# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTest2Suite(PerlPackage):
    """Distribution with a rich set of tools built upon the Test2 framework."""

    homepage = "https://metacpan.org/pod/Test2::Suite"
    url = "https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Suite-0.000159.tar.gz"

    maintainers("EbiArnie")

    version("0.000159", sha256="cb7453380d2a70682c450cb6ec44fecd02d1c48674a76d9799903b7f4444cc0e")

    depends_on("perl@5.8.1:", type=("build", "link", "run", "test"))
    depends_on("perl-term-table@0.013:", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
