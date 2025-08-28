#!/usr/bin/env python3
import argparse, json, logging, sys, hashlib, time
from datetime import datetime
from pathlib import Path

def setup_logging(verbosity:int=1, logfile: str=None):
    level = logging.INFO if verbosity <= 1 else logging.DEBUG
    handlers = [logging.StreamHandler(sys.stdout)]
    if logfile:
        Path(logfile).parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(logfile, encoding='utf-8'))
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s', handlers=handlers)

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def read_any(path: Path):
    txt = path.read_text(encoding='utf-8')
    try:
        return json.loads(txt), 'json'
    except json.JSONDecodeError:
        return {'raw_text': txt}, 'text'

def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding='utf-8')

def my_task(input_path: str, output_path: str) -> None:
    """Reusable task: read text/JSON → normalize → write JSON with metadata."""
    inp = Path(input_path)
    if not inp.exists():
        inp.parent.mkdir(parents=True, exist_ok=True)
        inp.write_text('{"message":"placeholder created"}', encoding='utf-8')
        logging.warning('Input %s not found; created placeholder', inp)
    data, kind = read_any(inp)
    payload = {
        'payload': data,
        'meta': {
            'kind': kind,
            'input_path': str(inp),
            'input_bytes': inp.stat().st_size,
            'timestamp_utc': datetime.utcnow().isoformat(timespec='seconds') + 'Z'
        }
    }
    out = Path(output_path)
    write_json(out, payload)
    logging.info('Wrote %s (%d bytes; sha256=%s)', out, out.stat().st_size, sha256_bytes(out.read_bytes()))

def main(argv=None):
    p = argparse.ArgumentParser(description='Refactor Demo: my_task CLI')
    p.add_argument('--input', required=True, help='Input file (text or JSON)')
    p.add_argument('--output', required=True, help='Output JSON path')
    p.add_argument('-v','--verbose', action='count', default=1, help='Increase verbosity')
    p.add_argument('--logfile', default=None, help='Optional log file path')
    args = p.parse_args(argv)
    setup_logging(args.verbose, args.logfile)
    my_task(args.input, args.output)

if __name__ == '__main__':
    main()