#!/bin/sh


echo "리눅스가 재미있나요? (yes / no)"
read answer

case "$answer" in
  [Yy] | [Yy][Ee][Ss] | *yes* )
    echo "yes"
    ;;
  [Nn] | [Nn][Oo] | *no* )
    echo "no"
    ;;
  *)
    echo "yes 또는 no로 입력해 주세요."
    ;;
esac

exit 0
