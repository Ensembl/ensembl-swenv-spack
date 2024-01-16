# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlEmailStuffer(PerlPackage):
    """A more casual approach to creating and sending Email:: emails"""

    homepage = "https://metacpan.org/pod/Email::Stuffer"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Stuffer-0.020.tar.gz"

    maintainers("EbiArnie")

    version("0.020", sha256="0a1efb7f2dedd39052b126f718ca2d3b5845a4123a39392fd9dfa0c76e6057c7")

    depends_on("perl@5.12.0:", type=("build", "link", "run", "test"))
    depends_on("perl-email-mime@1.943:", type=("run"))
    depends_on("perl-email-sender", type=("run", "test"))
    depends_on("perl-module-runtime", type=("run"))
    depends_on("perl-moo", type=("test"))
    depends_on("perl-params-util@1.05:", type=("run"))
    depends_on("perl-test-fatal", type=("test"))
