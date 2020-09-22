// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Filestore.Outputs
{

    [OutputType]
    public sealed class InstanceFileShares
    {
        /// <summary>
        /// File share capacity in GiB. This must be at least 1024 GiB
        /// for the standard tier, or 2560 GiB for the premium tier.
        /// </summary>
        public readonly int CapacityGb;
        /// <summary>
        /// The name of the fileshare (16 characters or less)
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Nfs Export Options. There is a limit of 10 export options per file share.
        /// Structure is documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.InstanceFileSharesNfsExportOption> NfsExportOptions;

        [OutputConstructor]
        private InstanceFileShares(
            int capacityGb,

            string name,

            ImmutableArray<Outputs.InstanceFileSharesNfsExportOption> nfsExportOptions)
        {
            CapacityGb = capacityGb;
            Name = name;
            NfsExportOptions = nfsExportOptions;
        }
    }
}
