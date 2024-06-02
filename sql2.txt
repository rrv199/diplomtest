(.venv) PS C:\Users\user\PycharmProjects\yandex_api_stand_tests2> ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\user/.ssh/id_rsa):
C:\Users\user/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\user/.ssh/id_rsa.
Your public key has been saved in C:\Users\user/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:VE4k6ny/qJ+BulqhWrzwMUL64SlMOW0VcWsYPf+gK5k user@DESKTOP-BBM317L
The key's randomart image is:
+---[RSA 3072]----+
|     .++.=       |
|     .oo+ .      |
|     +.. o       |
|o= + . + . .     |
|.X B E . + .     |
|..B.o.oo+ .      |
+----[SHA256]-----+
(.venv) PS C:\Users\user\PycharmProjects\yandex_api_stand_tests2> cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDPgedJnp5Ns/Ew6O7Pb+umcntyiop4BzEzu7LD5jQl1kuDPxN53fBUqwP19sCN03ioWpYtgmnRq4LtiA2mBJ2Vo6mFzvBWS2NOKdcTMkRyi3vBm7RPqgkZ7lzsGgnmWjVlBfPBnXxAU/OFX+iz60ilYJ4FqZ7eYmn9AwGyOfXEpnfg9UktuCyOGsvf5pBNlNV9F1aJ4Jw55vOiU0Ixd0VPDgAzmuMxvDshCg5CKscxA3jlSidADJDuRXi/nYaUkZdbWlSMEoFRFFopDnZcrPJeI+9d/vUkOtaFlnSbVdCf0/D8PW1/cESq23CW5T0fxekLTerwEhoyqRnR15KnVDVsXdgCrlq2eJsJcg2aIn0hfbvQUbhnY7PIzBzdEM6wvFUSfAVJrKJCnAV7YIA84Cg2kb5qTk9Nni/UAZqZZPVe45WMLoAT4V3xrxLcDlVArsnB9tMLBdm0H2qeTqcVGQ/rq02BRpuFHE8Iq4BAV0Qedrs5goScCVzc4BrYQOMslt8= user@DESKTOP-BBM317L
(.venv) PS C:\Users\user\PycharmProjects\yandex_api_stand_tests2> ssh 6b40e98d-4429-4052-b439-6f1ac6a05465@serverhub.praktikum-services.ru -p 4554
6b40e98d-4429-4052-b439-6f1ac6a05465@serverhub.praktikum-services.ru: Permission denied (publickey).
(.venv) PS C:\Users\user\PycharmProjects\yandex_api_stand_tests2> ssh 55c6e7e9-9466-405a-bc22-4678e49bb8b9@serverhub.praktikum-services.ru -p 4554
morty@7ebddc9f5406:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.
scooter_rent=# \dt+
                         List of relations
 Schema |     Name      | Type  | Owner |    Size    | Description
--------+---------------+-------+-------+------------+-------------
 public | Couriers      | table | root  | 8192 bytes |
 public | Orders        | table | root  | 8192 bytes |
 public | SequelizeMeta | table | root  | 8192 bytes |
(3 rows)
scooter_rent=# SELECT * FROM "Orders";
 id | courierId | firstName | lastName | address | metroStation | phone | rentTime | deliveryDate | track | inDelivery | color | comment | cancelled | finished | createdAt | updatedAt
----+-----------+-----------+----------+---------+--------------+-------+----------+--------------+-------+------------+-------+---------+-----------+----------+-----------+-----------
(0 rows)
scooter_rent=# SELECT "courierId" FROM "Orders" WHERE "inDelivery" = true;
 courierId
-----------
(0 rows)
scooter_rent=# SELECT "id", CASE WHEN finished == true THEN "2", WHEN canсelled == true THEN "-1", WHEN inDelivery == true THEN "1" END, FROM "Orders";
id
-----------
(0 rows)