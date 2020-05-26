// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Diagflow.Outputs
{

    [OutputType]
    public sealed class EntityTypeEntity
    {
        /// <summary>
        /// A collection of value synonyms. For example, if the entity type is vegetable, and value is scallions, a synonym
        /// could be green onions.
        /// For KIND_LIST entity types:
        /// * This collection must contain exactly one synonym equal to value.
        /// </summary>
        public readonly ImmutableArray<string> Synonyms;
        /// <summary>
        /// The primary value associated with this entity entry. For example, if the entity type is vegetable, the value
        /// could be scallions.
        /// For KIND_MAP entity types:
        /// * A reference value to be used in place of synonyms.
        /// For KIND_LIST entity types:
        /// * A string that can contain references to other entity types (with or without aliases).
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private EntityTypeEntity(
            ImmutableArray<string> synonyms,

            string value)
        {
            Synonyms = synonyms;
            Value = value;
        }
    }
}