// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.OsConfig.Inputs
{

    public sealed class GuestPoliciesPackageGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Default is INSTALLED. The desired state the agent should maintain for this recipe.
        /// INSTALLED: The software recipe is installed on the instance but won't be updated to new versions.
        /// INSTALLED_KEEP_UPDATED: The software recipe is installed on the instance. The recipe is updated to a higher version,
        /// if a higher version of the recipe is assigned to this instance.
        /// REMOVE: Remove is unsupported for software recipes and attempts to create or update a recipe to the REMOVE state is rejected.
        /// Default value is `INSTALLED`.
        /// Possible values are `INSTALLED`, `UPDATED`, and `REMOVED`.
        /// </summary>
        [Input("desiredState")]
        public Input<string>? DesiredState { get; set; }

        /// <summary>
        /// Type of package manager that can be used to install this package. If a system does not have the package manager,
        /// the package is not installed or removed no error message is returned. By default, or if you specify ANY,
        /// the agent attempts to install and remove this package using the default package manager.
        /// This is useful when creating a policy that applies to different types of systems.
        /// The default behavior is ANY.
        /// Default value is `ANY`.
        /// Possible values are `ANY`, `APT`, `YUM`, `ZYPPER`, and `GOO`.
        /// </summary>
        [Input("manager")]
        public Input<string>? Manager { get; set; }

        /// <summary>
        /// Unique identifier for the recipe. Only one recipe with a given name is installed on an instance.
        /// Names are also used to identify resources which helps to determine whether guest policies have conflicts.
        /// This means that requests to create multiple recipes with the same name and version are rejected since they
        /// could potentially have conflicting assignments.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GuestPoliciesPackageGetArgs()
        {
        }
    }
}
