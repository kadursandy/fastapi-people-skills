from pydantic import BaseModel #EmailStr
from typing import List, Optional, Union, Literal

from pydantic.fields import Field


class Skill(BaseModel):
    skill_name: Literal['Python', 'DevOps', 'Ansible', 'Terraform']
    skill_level: int = Field(le=10, ge=1)


class Skills(BaseModel):
    skill_name: str = None
    skill_level: int = 0


class Python(Skills):
    skill_name = "Python"
    skill_level = 0


class DevOps(Skills):
    skill_name = "DevOps"
    skill_level = 0


class Ansible(Skills):
    skill_name = "Ansible"
    skill_level = 0


class Terraform(Skills):
    skill_name = "Terraform"
    skill_level = 0


class Person(BaseModel):
    name: str = "John Doe"
    # email: EmailStr
    age: int = 30
    # skills: List[Union[Python, DevOps, Ansible, Terraform]] = None
    skills: List[Skill]
