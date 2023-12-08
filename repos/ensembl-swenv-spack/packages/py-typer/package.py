# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-typer
#
# You can edit this file again by typing:
#
#     spack edit py-typer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyTyper(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "typer/typer-0.9.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("0.9.0", sha256="50922fd79aea2f4751a8e0408ff10d2662bd0c8bbfa84755a699f3bada2978b2")

    depends_on("py-flit-core", type="build")

    # FIXME: Add additional dependencies if required.
    depends_on("py-click", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-colorama", type=("build", "run"))
    depends_on("py-shellingham", type=("build", "run"))
    # TODO
    # depends_on("py-rich", type=("build", "run"))

