#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

import pytest
from k8s_test_harness.util import docker_util, env_util


@pytest.mark.parametrize("image_version", ("4.5.1", "4.6.1"))
def test_csi_attacher_rock(image_version):
    """Test csi-attacher rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "csi-attacher", image_version, "amd64"
    )
    image = rock.image

    # check binary.
    process = docker_util.run_in_docker(image, ["/csi-attacher", "--help"])
    assert "Usage of /csi-attacher" in process.stderr
