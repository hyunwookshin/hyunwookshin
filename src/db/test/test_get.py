#!/usr/bin/env python3

import boto3
import json
import decimal
import argparse
from boto3.dynamodb.conditions import Key, Attr

def parseArgs():
   parser = argparse.ArgumentParser()
   parser.add_argument( "-t", "--table", help="table name",
                        required=True )
   return parser.parse_args()

def testGet( tableName ):
   dynamodb_resource = boto3.resource('dynamodb')
   table = dynamodb_resource.Table( tableName )
   response = table.scan(
         FilterExpression=Key('section').eq( "about" )
      )
   print( response )

def main():
   args = parseArgs()
   testGet( args.table )

if __name__ == "__main__":
   main()
