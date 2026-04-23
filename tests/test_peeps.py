import pytest

from mawaland.peeps import Mawapeep, PeepRole


class TestMawaPeeps:
    def test_peep_role_is_none_when_created(self):
        peep = Mawapeep()

        assert peep.current_role is None


    @pytest.mark.parametrize(
        "fake_role",
        ["farmer", ["farmer"], {"role": "farmer"}]
    )
    def test_raises_error_when_role_not_a_member_of_peprole(self, fake_role):
        peep = Mawapeep()

        with pytest.raises(ValueError):
            peep.current_role = fake_role

    def tests_returns_correct_role_after_setting(self):
        peep = Mawapeep()
        peep.current_role = PeepRole.FARMER

        assert peep.current_role == PeepRole.FARMER