#!/bin/sh

function() {
	echo "함수 안으로 들어왔음"
	ls "$@"
	echo "함수 안에서 나감"
}

echo "프로그램을 시작합니다."

function "$@"

echo "프로그램을 종료합니다."

exit 0
