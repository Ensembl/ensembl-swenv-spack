# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlTestHarness(PerlPackage):
    """Test::Harness - Run Perl standard test scripts with statistics"""

    homepage = "https://metacpan.org/pod/Test::Harness"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/Test-Harness-3.44.tar.gz"

    maintainers("EbiArnie")

    version("3.45_02", sha256="d09a51528ac635663679c91f3628963e60ffbd56ffeee2ccf56112825a48fa04")
