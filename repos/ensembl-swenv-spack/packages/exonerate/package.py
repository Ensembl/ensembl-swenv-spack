# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Exonerate(AutotoolsPackage):
    """Exonerate - a generic tool for pairwise sequence alignment of DNA and proteins."""

    homepage = "https://www.ebi.ac.uk/about/vertebrate-genomics/software/exonerate"
    url = "https://github.com/sgiorgetti/exonerate.git"

    maintainers("sgiorgetti", "ebi_arnie")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # license("GPL-3.0-only", checked_by="sgiorgetti")

    version("2.4.1", git='https://github.com/sgiorgetti/exonerate.git', commit='eb05b8b')
    version("2.4.0", sha256="f849261dc7c97ef1f15f222e955b0d3daf994ec13c9db7766f1ac7e77baa4042")
    version("2.2.0", sha256="0ea2720b1388fa329f889522f43029b416ae311f57b229129a65e779616fe5ff")

    variant(
        "glib2",
        default=True,
        description="Compile with GLib2.0"
    )
    variant(
        "assert",
        default=False,
        description="Use code for assertion tests"
    )
    variant(
        "paranoia",
        default=False,
        description="Use paranoid compilation options"
    )
    variant(
        "largefile",
        default=True,
        description="Enable largefile support on 32 bit systems"
    )
    variant(
        "compiledmodels",
        default=True,
        description="Use compiled C4 models"
    )
    variant(
        "utilities",
        default=True,
        description="Install all utilities"
    )

    depends_on("autoconf", type="build", when="@2.4.1 build_system=autotools")
    depends_on("automake", type="build", when="@2.4.1 build_system=autotools")
    depends_on("libtool", type="build", when="@2.4.1 build_system=autotools")
    depends_on("pkgconfig", type="build")
    depends_on("glib")

    def url_for_version(self, version):
        url = "https://ftp.ebi.ac.uk/pub/software/vertebrategenomics/exonerate/exonerate-{0}.tar.gz"
        return url.format(version.up_to(3))

    @property
    def force_autoreconf(self):
        return self.version == Version("2.4.1")

    parallel = False

    def configure_args(self):
        config_args = []

        config_args.append("--disable-debug")
        config_args.append("--disable-dependency-tracking")
        config_args.extend(self.enable_or_disable("glib2"))
        config_args.extend(self.enable_or_disable("assert"))
        config_args.extend(self.enable_or_disable("paranoia"))
        config_args.extend(self.enable_or_disable("largefile"))
        config_args.extend(self.enable_or_disable("compiledmodels"))
        config_args.extend(self.enable_or_disable("utilities"))

        return config_args

