# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetimeTimezone(PerlPackage):
    """Time zone object base class and factory"""

    homepage = "https://metacpan.org/pod/DateTime::TimeZone"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-2.60.tar.gz"

    maintainers("EbiArnie")

    version("2.60", sha256="f0460d379323905b579bed44e141237a337dc25dd26b6ab0c60ac2b80629323d")

    depends_on("perl@5.8.4:", type=("build", "link", "run", "test"))
    depends_on("perl-class-singleton@1.03:", type=("run"))
    depends_on("perl-module-runtime", type=("run"))
    depends_on("perl-namespace-autoclean", type=("run"))
    depends_on("perl-params-validationcompiler@0.13:", type=("run"))
    depends_on("perl-specio", type=("run"))
    depends_on("perl-test-fatal", type=("test"))
    depends_on("perl-test-requires", type=("test"))
    depends_on("perl-try-tiny", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
