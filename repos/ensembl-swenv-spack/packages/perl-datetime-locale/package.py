# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetimeLocale(PerlPackage):
    """Localization support for DateTime.pm"""

    homepage = "https://metacpan.org/pod/DateTime::Locale"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-1.39.tar.gz"

    maintainers("EbiArnie")

    version("1.39", sha256="10c145a6c7daf7118864e97482b4ae9f94f93b9414212eee8aa30b16a8135100")

    depends_on("perl@5.8.4:", type=("build", "link", "run", "test"))
    depends_on("perl-cpan-meta-check@0.011:", type=("test"))
    depends_on("perl-dist-checkconflicts@0.02:", type=("build", "run"))
    depends_on("perl-file-sharedir", type=("run"))
    depends_on("perl-file-sharedir-install@0.06:", type=("build"))
    depends_on("perl-ipc-system-simple", type=("test"))
    depends_on("perl-namespace-autoclean@0.19:", type=("run"))
    depends_on("perl-params-validationcompiler@0.13:", type=("run"))
    depends_on("perl-path-tiny", type=("test"))
    depends_on("perl-specio", type=("run"))
    depends_on("perl-test-file-sharedir", type=("test"))
    depends_on("perl-test2-plugin-nowarnings", type=("test"))
    depends_on("perl-test2-suite", type=("test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
