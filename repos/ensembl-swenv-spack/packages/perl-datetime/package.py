# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetime(PerlPackage):
    """A date and time object for Perl"""

    homepage = "https://metacpan.org/pod/DateTime"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-1.63.tar.gz"

    maintainers("EbiArnie")

    version("1.63", sha256="1b11e49ec6e184ae2a10eccd05eda9534f32458fc644c12ab710c29a3a816f6f")

    depends_on("perl@5.8.4:", type=("build", "link", "run", "test"))
    depends_on("perl-cpan-meta-check@0.011:", type=("test"))
    depends_on("perl-datetime-locale@1.06:", type=("run"))
    depends_on("perl-datetime-timezone@2.44:", type=("run"))
    depends_on("perl-dist-checkconflicts@0.02:", type=("build", "run"))
    depends_on("perl-namespace-autoclean@0.19:", type=("run"))
    depends_on("perl-params-validationcompiler@0.26:", type=("run"))
    depends_on("perl-specio@0.18:", type=("run"))
    depends_on("perl-test-fatal", type=("test"))
    depends_on("perl-test-warnings@0.005:", type=("test"))
    depends_on("perl-test-without-module", type=("test"))
    depends_on("perl-try-tiny", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
