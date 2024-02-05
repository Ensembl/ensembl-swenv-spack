# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlEmailDateFormat(PerlPackage):
    """Produce RFC 2822 date strings"""

    homepage = "https://metacpan.org/pod/Email::Date::Format"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-Format-1.008.tar.gz"

    maintainers("EbiArnie")

    version("1.008", sha256="432b7c83ff88749af128003f5257c573aec1a463418db90ed22843cbbc258b4f")
    version("1.007", sha256="5956d953f3e2f8e6f614304df3be30399721b0f0f9a2407fd68b74a68ff62e52")

    depends_on("perl@:5.29.0", when="@:1.007", type=("build", "link", "run", "test"))
    depends_on("perl@5.29.1:", when="@1.008:", type=("build", "link", "run", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Email::Date::Format; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
