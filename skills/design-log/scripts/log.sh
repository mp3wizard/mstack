#!/usr/bin/env bash
# Append one row to a design-log decision log (TSV).
# Usage: log.sh <logfile> <phase> <decision> <why> <evidence> <tier> <result>
#        log.sh --self-test
set -euo pipefail

HEADER=$'ts\tphase\tdecision\twhy\tevidence\ttier\tresult'

# Cells stay on one line. A cell a spreadsheet would read as a formula
# (=, +, -, @), even after leading spaces an importer may trim, gets a
# leading single quote, because evidence can come from page titles,
# filenames, or participant text.
clean() {
	local v t
	v=$(printf '%s' "$1" | tr '\t\n\r' '   ')
	t="${v#"${v%%[! ]*}"}"
	case "$t" in
		=*|+*|-*|@*) printf "'%s" "$v" ;;
		*) printf '%s' "$v" ;;
	esac
}

append() {
	local logfile="$1"
	shift
	local logdir
	logdir="$(dirname "$logfile")"
	if [ -n "$logdir" ] && [ "$logdir" != "." ] && [ ! -d "$logdir" ]; then
		mkdir -p "$logdir"
	fi
	# Append with >> even for the header, so a false "empty" reading on a
	# network mount costs one stray header line, never the existing rows.
	if [ ! -s "$logfile" ]; then
		printf '%s\n' "$HEADER" >> "$logfile"
	fi
	local ts
	ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
	printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$ts" \
		"$(clean "$1")" "$(clean "$2")" "$(clean "$3")" "$(clean "$4")" "$(clean "$5")" "$(clean "$6")" \
		>> "$logfile"
}

self_test() {
	local dir log
	dir="$(mktemp -d)"
	log="$dir/sub/decisions.tsv"
	append "$log" frame "scoped the checkout redesign" "size before a long run" "screens/inventory.md" 1 open
	append "$log" "=evil()" $'two\tcells\nhere' "+1" "@x" "-2" $'\t=x'
	[ "$(head -1 "$log")" = "$HEADER" ] || { echo "self-test: header missing" >&2; exit 1; }
	[ "$(wc -l < "$log" | tr -d ' ')" = "3" ] || { echo "self-test: expected 3 lines" >&2; exit 1; }
	local row
	row="$(sed -n 3p "$log")"
	[ "$(printf '%s' "$row" | awk -F'\t' '{print NF}')" = "7" ] || { echo "self-test: expected 7 cells" >&2; exit 1; }
	printf '%s' "$row" | awk -F'\t' '$2=="'"'"'=evil()" && $3=="two cells here" && $4=="'"'"'+1" && $5=="'"'"'@x" && $6=="'"'"'-2" && $7=="'"'"' =x" {ok=1} END {exit !ok}' \
		|| { echo "self-test: cells not cleaned" >&2; exit 1; }
	rm -rf "$dir"
	echo "log.sh self-test: ok"
}

if [ "${1:-}" = "--self-test" ]; then
	self_test
	exit 0
fi

if [ "$#" -ne 7 ]; then
	printf 'usage: log.sh <logfile> <phase> <decision> <why> <evidence> <tier> <result>\n       log.sh --self-test\n' >&2
	exit 1
fi

append "$@"
