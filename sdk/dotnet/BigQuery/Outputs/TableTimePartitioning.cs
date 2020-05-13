// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.BigQuery.Outputs
{

    [OutputType]
    public sealed class TableTimePartitioning
    {
        /// <summary>
        /// Number of milliseconds for which to keep the
        /// storage for a partition.
        /// </summary>
        public readonly int? ExpirationMs;
        /// <summary>
        /// The field used to determine how to create a range-based
        /// partition.
        /// </summary>
        public readonly string? Field;
        /// <summary>
        /// If set to true, queries over this table
        /// require a partition filter that can be used for partition elimination to be
        /// specified.
        /// </summary>
        public readonly bool? RequirePartitionFilter;
        /// <summary>
        /// The only type supported is DAY, which will generate
        /// one partition per day based on data loading time.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private TableTimePartitioning(
            int? expirationMs,

            string? field,

            bool? requirePartitionFilter,

            string type)
        {
            ExpirationMs = expirationMs;
            Field = field;
            RequirePartitionFilter = requirePartitionFilter;
            Type = type;
        }
    }
}