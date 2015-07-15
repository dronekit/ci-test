#!/bin/bash

a() { set -e; return $CI_EXIT; }
z() { E=$?; CI_EXIT=$E || $CI_EXIT; test $E -eq 0 || echo 'STOP>>>'; return $CI_EXIT; }
zz() { E=$?; CI_EXIT=$E || $CI_EXIT; test $E -eq 0 || echo 'STOP>>>'; return $CI_EXIT; }

(a; echo HI );z;
(a; false );z;
(a; echo HI );z;
(a; true );zz;
