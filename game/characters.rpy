## Dynamic Character Variables
define protag_name = "Placeholder"
define robot_name = "Robot"
define android_name = "Android"
define cryptid_name = "Cryptid"

## Base Character
define base = Character()

## Main Characters
define protagonist = Character("protag_name", dynamic=True, kind=base)
define alban = Character("Alban Knox", kind=base)
define fulgur = Character("Fulgur Ovid", kind=base)
define sonny = Character("Sonny Brisko", kind=base)
define uki = Character("Uki Violeta", kind=base)

## Mascots/Animals
define briskadet = Character("Briskadet", kind=base)
define comfydant = Character("Comfydant", kind=base)
define stargazer = Character("Stargazer", kind=base)
define takaradachi = Character("Takaradachi", kind=base)

define bleep_bleep = Character("Bleep Bleep", kind=base)
define sheero = Character("Sheero", kind=base)
define ukinya = Character("Ukinya", kind=base)
define dog = Character("Dog", kind=base)
define cat = Character("Cat", kind=base)
define kat = character("Kat", kind=base)

## Enemies
define robot = Character("robot_name", dynamic=True, kind=base)
define android = Character("android_name", dynamic=True, kind=base)
define cryptid = Character("cryptid_name", dynamic=True, kind=base)
define virus = Character("Virus", kind=base)
