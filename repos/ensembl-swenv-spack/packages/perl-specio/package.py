# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlSpecio(PerlPackage):
    """Type constraints and coercions for Perl"""

    homepage = "https://metacpan.org/pod/Specio"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.48.tar.gz"

    maintainers("EbiArnie")

    version("0.48", sha256="0c85793580f1274ef08173079131d101f77b22accea7afa8255202f0811682b2")

    depends_on("perl@5.8.0:", type=("build", "link", "run", "test"))
    depends_on("perl-devel-stacktrace", type=("run"))
    depends_on("perl-eval-closure", type=("run"))
    depends_on("perl-module-runtime", type=("run"))
    depends_on("perl-mro-compat", type=("run"))
    depends_on("perl-role-tiny@1.003003:", type=("run"))
    depends_on("perl-sub-quote", type=("run"))
    depends_on("perl-test-fatal", type=("run"))
    depends_on("perl-test-needs", type=("test"))
    depends_on("perl-try-tiny", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
