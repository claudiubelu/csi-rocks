#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util

ROCK_EXPECTED_FILES = [
    "/bin/pebble",
]


def test_csi_attacher_rock():
    """Test csi-attacher rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "csi-attacher", "4.5.1", "amd64"
    )
    image = rock.image

    # check rock filesystem.
    docker_util.ensure_image_contains_paths(image, ROCK_EXPECTED_FILES)
