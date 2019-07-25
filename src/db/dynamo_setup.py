#!/usr/bin/env python3

import sys
import boto3
import argparse
import json

def parseArgs():
   parser = argparse.ArgumentParser()
   parser.add_argument( "-c", "--check", help="check if table created",
                        action="store_true", required=False )
   parser.add_argument( "-a", "--add", help="insert data entry",
                        action="store_true", required=False )
   parser.add_argument( "-t", "--table", help="table name",
                        required=True )
   parser.add_argument( "-p", "--partition", help="partition key name",
                        required=True )
   parser.add_argument( "-s", "--sort", help="sort key name",
                        required=True )
   parser.add_argument( "-j", "--json", help="input JSON",
                        required=False )
   return parser.parse_args()

def addEntry( table, info ):
   return table.put_item(Item=info)

def collectInfo( info ):
   ans = ""
   while ans != "q":
      ans = input( "Enter colume value pair separated by ':' or 'q' to quit:\n" )
      if ":" not in ans:
         print( "Please enter colon!")
         continue
      col, value = ans.split(":")
      info[ col.strip() ] = value.strip()

def main():
   args = parseArgs()
   dynamodb_client = boto3.client('dynamodb')
   dynamodb_resource = boto3.resource('dynamodb')
   tableName = args.table
   tableNames = dynamodb_client.list_tables()['TableNames']
   if args.check:
      if tableName not in tableNames:
         print(tableName, "is not present! Please create one in AWS console")
      else:
         print(tableName, "is present!")
   elif args.add:
      # eventually be done through the web UI
      table = dynamodb_resource.Table( tableName )
      info = {}
      if args.json:
         info = json.loads( args.json )
      else:
         collectInfo( info )
      if args.partition not in info:
         print( "Partition key, {}, not found here!".format( args.partition ) )
         return
      elif args.sort not in info:
         print( "Sort key, {}, not found here!".format( args.partition ) )
         return
      print( addEntry( table, info ) )
   else:
      print( "No action found" )
      return

if __name__ == "__main__":
   main()
